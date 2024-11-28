const highlightedItems = document.querySelectorAll("img");

highlightedItems.forEach((userItem) => {
  userItem.addEventListener("click", function() {
    window.open(userItem.src, "_blank");
  })
});