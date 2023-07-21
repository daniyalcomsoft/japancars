
const carsDataBox = document.getElementById('companyddl')
const carInput = document.getElementById('cars')

// $.ajax({
//     type: 'GET',
//     url: '/carbydropdown/',
//     success: function(response){
//         console.log(response.data)
//         const carsData = response.data
//         carsData.map(item=>{
//             const option = document.createElement('div')
//             option.textContent = item.name
//             option.setAttribute('class', 'item')
//             option.setAttribute('data-value', item.name)
//             carsDataBox.appendChild(option)

//         })
//     },
//     error: function(error){
//         console.log(error)
//     }
// })