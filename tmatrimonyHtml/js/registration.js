$("#registrationSubmit").click(function(e) {
  e.preventDefault();
  var first_name = $("#firstName").val(); 
  var middle_name = $("#middleName").val();
  var last_name = $("#lastName").val();
  var age = $("#age").val();
  var height = $("#height").val();
  var color = $("#color").val();
  var religion = $("#religion").val();
  var caste = $("#caste").val(); 
  var dataString = 'firstName='+first_name+'&middleName='+middle_name+'&lastName='+last_name+'&age='+age+'&height='+height+'&color='+color+'&religion='+religion+'&caste='+caste;
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
        tableData=tableData+'<tr><td>'+data[i].first_name+'</td><td>'+data[i].last_name+'</td><td>'+data[i].age+'</td><td>'+data[i].height+'</td><td>'+data[i].color+'</td><td>'+data[i].religion+'</td><td>'+data[i].caste+'</td></tr>';
      }
      $('#tbody').html(tableData);
      //alert(data);
    }
  });    
});
