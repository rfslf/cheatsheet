categoryColorPalette = ["#90EE90", "#B0C4DE", "#FFA07A", "#DC143C", "#D2B48C", "#FFD700", "#000000"]

//Сделать плитки категории цветными
window.addEventListener('DOMContentLoaded', event => {
    var categories = document.body.querySelectorAll(".category");
    var iter = 0
    categories.forEach(category => {
        paletteIter = iter % 5
        category.style.backgroundColor = categoryColorPalette[paletteIter]
        category.addEventListener('mouseover', event => {
            category.style.color = categoryColorPalette[6]
        });
        iter =+ 1
    });
});
