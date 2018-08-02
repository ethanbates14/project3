function getParentModal(e) {
    var elem = e.closest('.modal').id;
    return elem;
};

function getQuantity(parentElem) {
    let parent = document.getElementById(parentElem);
    var qty = parent.querySelector('.input-quantity').value;
    return qty;
};

function getCheckedRadio(parentElem) {
    let parent = document.getElementById(parentElem);

    radioButtons = parent.querySelectorAll('.input-price');

    for (var i = 0; i < radioButtons.length; i++) {
        if (radioButtons[i].checked == true) {
            var itemSelect = radioButtons[i].id;
            var itemAmt = radioButtons[i].value;
            return [itemSelect,itemAmt];
        };
    };

};


document.addEventListener('DOMContentLoaded', function() {

  // Add to Cart
  document.querySelectorAll('.add-to-cart').forEach(function(item) {
    item.onclick = function() {
        pModal = getParentModal(item);
        itemCount = getQuantity(pModal);
        itemChose = getCheckedRadio(pModal);

        if ( (itemCount>0)&& (itemChose !=null) ) {

            console.log('Adding ' + itemCount + ' ' + itemChose[1] + ' to cart');
        }
    };
  });

}); //DOM-READY
