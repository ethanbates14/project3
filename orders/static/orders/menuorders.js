function getParentModal(e) {
    var elem = e.closest('.modal').id;
    return elem;
};

function getQuantity(parentElem) {
    let parent = document.getElementById(parentElem);
    var qty = parent.querySelector('.input-quantity').value;
    return qty;
};

function getItemName(parentElem) {
    let parent = document.getElementById(parentElem);
    var itemName = parent.querySelector('.modal-title').innerHTML;
    return itemName;
};

//Toppings Max Checks
function toppingCheck(parentElem) {
    let parent = document.getElementById(parentElem);
    toppingList = parent.querySelectorAll('.input-toppings');
    t_list = []

    for (var i = 0; i < toppingList.length; i++) {
        if (toppingList[i].checked == true) {
            var itemString = toppingList[i].nextElementSibling.innerText;
            t_list.push(itemString);
        };
    };
    return t_list;
};


function getCheckedRadio(parentElem) {
    let parent = document.getElementById(parentElem);

    radioButtons = parent.querySelectorAll('.input-price');

    for (var i = 0; i < radioButtons.length; i++) {
        if (radioButtons[i].checked == true) {
            var menu_id = radioButtons[i].id;
            var itemAmount = radioButtons[i].value;
            var itemString = radioButtons[i].nextElementSibling.innerText;
            return [menu_id,itemAmount,itemString];
        };
    };
};

function updateTotal(addNum,multiplier) {
    var orderAmt = document.querySelector('#total-order-cost');
    var currentTotal = parseFloat(orderAmt.innerText);
    var newTotal = currentTotal + parseFloat(addNum*multiplier);
    orderAmt.innerText = newTotal.toFixed(2);
};


document.addEventListener('DOMContentLoaded', function() {

  // Add to Cart
  document.querySelectorAll('.add-to-cart').forEach(function(item) {
    item.onclick = function() {
        pModal = getParentModal(item);
        pItem = getItemName(pModal);
        itemCount = getQuantity(pModal);
        itemChose = getCheckedRadio(pModal);
        pToppings = toppingCheck(pModal);
        console.log(pToppings[0]);


        if ( (itemCount>0)&& (itemChose !=null) ) {
            console.log('Adding ' + itemCount + ' ' + itemChose[1] + ' to cart');
            var NewItem = document.createElement('input');
            NewItem.setAttribute("type","text");
            NewItem.setAttribute("class","form-control-plaintext new-cart-item");
            NewItem.setAttribute("placeholder",itemCount + ' ' + pItem + ' @' + itemChose[2])
            NewItem.readOnly = true;

            document.querySelector("#order-list").appendChild(NewItem);
            updateTotal(itemChose[1],itemCount[0]);

        }
    };
  });


}); //DOM-READY
