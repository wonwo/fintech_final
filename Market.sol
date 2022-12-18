// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract MarketPlaceTOD{
    address payable owner;
    uint private price;
    uint private itemQunatity;
    uint private total;
    
    mapping (address => uint) private balances;
    mapping (address => uint) private ownQuantity;
    
    modifier onlyOwner(){
        require(msg.sender == owner);
        _;
    }
    
    event UpdatePrice(uint _price);
    event UpdateStock(uint _quantity);
    event Buy(uint _price, uint _quantity, uint _value);
    
    constructor(uint setPrice, uint setItemQunatity) {
        owner = payable(msg.sender);
        price = setPrice;
        itemQunatity = setItemQunatity;
    }
    
    //Owner update price
    function updatePrice(uint newPrice) public onlyOwner{
        price = newPrice;
        emit UpdatePrice(price);
    }
    
    //Owner update Quantity
    function updateQuantity(uint newQuantity) public onlyOwner{
        itemQunatity = newQuantity;
        emit UpdateStock(itemQunatity);
    }
    
    //Check price
    function checkPrice() public view returns(uint){
        return price;
    }
    
    //Check quantity
    function checkQuantity() public view returns(uint){
        return itemQunatity;
    }
    
    function buy(uint buyQuantity) public {
        total = price * buyQuantity;
        require(balances[msg.sender] > total);
        require(itemQunatity > buyQuantity);
        itemQunatity -= buyQuantity;

        balances[msg.sender] -= total;
        ownQuantity[msg.sender] += buyQuantity;
        balances[owner] += total;
        
        emit Buy(price , buyQuantity , total);
    }

    //Owner give token
    function issue(address account, uint amount) public onlyOwner{
        balances[account] += amount;
    }

    function checkAddressBalance(address account) public view returns(uint){
        return balances[account];
    }

    function checkAddressQunatity(address account) public view returns(uint){
        return ownQuantity[account];
    }
}