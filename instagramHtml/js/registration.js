$("#registrationSubmit").click(function(e) {
  e.preventDefault();
  var first_name = $("#firstName").val(); 
  var middle_name = $("#middleName").val();
  var last_name = $("#lastName").val();
  var mobile_number = $("#mobileNumber").val();
  var email= $("#email").val();
  var password = $("#password").val();
  var re_enterpassword = $("#reEnterpassword").val();
  var caste = $("#caste").val(); 
  var dataString = 'firstName='+first_name+'&middleName='+middle_name+'&lastName='+last_name+'&mobileNumber='+mobile_number+'&email='+email+'&password='+passwordr+'&reEnterpassword='+re_enterpassword+;
  console.log(dataString);
  $.ajax({
    type:'POST',
    data:dataString,
    url:'http://127.0.0.1:8000/registration/',
    success:function(data) {
      alert(data);
    }
  });
});

$( document ).ready(function() {
  $.ajax({
    type:'GET',
    //data:dataString,
    url:'http://127.0.0.1:8000/registration/',
    success:function(data) {
      var tableData;
      for(i=0;i<(data.length-1);i++){
        console.log(data[1]);
        tableData=tableData+'<tr><td>'+data[i].first_name+'</td><td>'+data[i].last_name+'</td><td>'+data[i].mobile_number+'</td><td>'+data[i].email+'</td><td>'+data[i].password+'</td><td>'+data[i].re_enterpassword+'</td><td>';
      }
      $('#tbody').html(tableData);
      //alert(data);
    }
  });    
});
