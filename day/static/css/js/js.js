document.addEventListener("DOMContentLoaded", function () {
    // Select elements
    const contentPara = document.getElementById("con");
    const plusBtn = document.querySelector(".quantity-btn:last-of-type"); // "+" button
    const minusBtn = document.querySelector(".quantity-btn:first-of-type"); // "-" button
    const inputField = document.getElementById("val");

    // Extract initial price from content (assuming it's like "Price: ₹100")
    let basePrice = parseInt(contentPara.textContent.match(/\d+/)[0]); 
    let totalPrice = basePrice;

    // Function to update price
    function updatePrice() {
        contentPara.innerHTML = `<b>Price: ₹${totalPrice}</b>`;
    }

    // Event listener for "+"
    plusBtn.addEventListener("click", function () {
        let currentValue = parseInt(inputField.value);
        currentValue++;
        inputField.value = currentValue;

        totalPrice = currentValue * basePrice;
        updatePrice();
    });

    // Event listener for "-"
    minusBtn.addEventListener("click", function () {
        let currentValue = parseInt(inputField.value);
        if (currentValue > 1) {
            currentValue--;
            inputField.value = currentValue;

            totalPrice = currentValue * basePrice;
            updatePrice();
        }
    });

    // Initialize the default price display
    updatePrice();
});
