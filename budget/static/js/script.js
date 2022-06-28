(function (params) {
   document.querySelector('#categoryInput').addEventListener('keydown', function(e){
    if(e.keyCode != 13){
        return;
    }

    e.preventDefault()

    var categoryName = this.value
    this.value = ''
    addNewCategory(categoryName)
    updateCategoriesString()

   }) 

   function addNewCategory(name){
    document.querySelector('#categoriesContainer').insertAdjacentHTML('beforeend',
    `<li class="category">
            <span class="name">${name}</span>
            <span onclick="removeCategory(this)" class="btnRemove bold">remove</span>
        </li>`)
   }
})()


function fetchCategoryArray() {
    var categories = []

    document.querySelectorAll('.category').forEach( function(e){
        category_name = e.querySelector('.name').innerHTML
        if(category_name == '') return;

        categories.push(category_name)
    } )

    return categories
}

function updateCategoriesString() {
categories = fetchCategoryArray()
document.querySelector('input[name = "categoriesString"]').value = categories.join(',')
}

function removeCategory(e) {
    e.parentElement.remove()
    updateCategoriesString()
}