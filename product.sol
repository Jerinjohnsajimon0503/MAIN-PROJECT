// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Product {
    
    
    struct Medicine {
        
        
        string name;
        string dosage;
        string price;
        string indgredient;
        string route;
        string manufaturerName;
        string maddress;
        string mcountry;
       
        string mphone;
       
    }

    struct Status {
        
        
        string name;
        string status;
        string location;
        string date;
    }

    Medicine[] public medicineDetails; 
    Status[] public status; 

    function retrieve() public view returns (Medicine[] memory){
        return medicineDetails; 
    }

    function retrieveStatus() public view returns (Status[] memory){
        return status; 
    }
    
    function addProduct(string memory _name,string memory _dosage,string memory _price,string memory _indgredient,string memory _route,string memory _manufaturerName,string memory _maddress,string memory _mcountry,string memory _mphone) public {
        medicineDetails.push(Medicine(_name,_dosage, _price, _indgredient,_route,_manufaturerName,_maddress,_mcountry,_mphone)); //append to  Contact[] array
        // nameToPhoneNumber[_name] = _phoneNumber; //use name to get phone number
    }
    
    function addStatus(string memory _name,string memory _status,string memory _location,string memory _date) public {
        status.push(Status(_name,_status,_location,_date)); //append to  Contact[] array
        // nameToPhoneNumber[_name] = _phoneNumber; //use name to get phone number
    }
    
}



