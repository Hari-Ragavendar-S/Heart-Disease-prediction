const form = document.getElementById('predictForm');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      resultDiv.style.display = 'block';
      resultDiv.className = 'alert alert-warning';
      resultDiv.innerHTML = '<div class="heart-loader"></div> Predicting... please wait...';

      const formData = new FormData(form);
      
      try {
        const response = await fetch('/predict', { 
          method: 'POST', 
          body: formData 
        });

        // Try to read JSON if Flask sends a prediction
        const contentType = response.headers.get('content-type');
        if (contentType && contentType.includes('application/json')) {
          const data = await response.json();
          
          if (data.prediction === 1) {
            resultDiv.className = 'alert alert-danger';
            resultDiv.textContent = 'High risk of Heart Disease detected. Downloading detailed report...';
          } else {
            resultDiv.className = 'alert alert-success';
            resultDiv.textContent = 'Low risk of Heart Disease. Downloading detailed report...';
          }

          // Also download report if available
          if (data.report_url) {
            window.location.href = data.report_url;
          }

        } else {
          // Otherwise assume it's a PDF file
          const blob = await response.blob();
          const link = document.createElement('a');
          link.href = window.URL.createObjectURL(blob);
          link.download = 'Heart_Disease_Report.pdf';
          document.body.appendChild(link);
          link.click();
          document.body.removeChild(link);

          resultDiv.className = 'alert alert-success';
          resultDiv.textContent = 'Report generated and downloaded successfully!';
        }
      } catch (err) {
        resultDiv.className = 'alert alert-danger';
        resultDiv.textContent = 'Error getting prediction or report. Please try again.';
        console.error(err);
      }
    });
 