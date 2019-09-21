function hideShowDeliveryForm() {

    var delivery = document.getElementsByid("delivery-form");
    
    if (delivery.style.display === "none") {
        delivery.style.display = "block";
    } else {
      delivery.style.display = "none";
    }
  }