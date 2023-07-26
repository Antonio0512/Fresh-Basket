document.addEventListener("DOMContentLoaded", function () {
    const stripe = Stripe("YOUR_STRIPE_PUBLIC_KEY");

    // Event listener for the checkout button
    document.getElementById("checkout-button").addEventListener("click", function () {
        fetch("/create-checkout-session/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken"), // Replace with the appropriate function to get the CSRF token
            },
        })
            .then(function (response) {
                return response.json();
            })
            .then(function (session) {
                return stripe.redirectToCheckout({sessionId: session.id});
            })
            .then(function (result) {
                if (result.error) {
                    alert(result.error.message);
                }
            });
    });
});
