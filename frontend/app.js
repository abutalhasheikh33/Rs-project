const postForm  = document.querySelector('.postForm')
const cardHolder = document.querySelector('.card-holder')
function postData(url = '') {
    // Default options are marked with *
    return fetch(url, {
      
      headers: {
        'Content-Type': 'application/json'
        // 'Content-Type': 'application/x-www-form-urlencoded',
      },
   
    })
    .then(response => response.json()); // parses JSON response into native JavaScript objects
  }



postForm.addEventListener('submit',(e)=>{
    e.preventDefault();
    postData('http://127.0.0.1:5000')

  .then(data => {
     // JSON data parsed by `response.json()` call
     
     console.log(data)
     for(let attr in data){
        
        cardHolder.innerHTML += `
        <div class="card">
        ${attr} :  ${data[attr]}
        </div>`;
      
     }

  })
  .catch(error => {
    console.error('Error:', error);
  });
})