$("#registrationSubmit").click(function(e) {
  e.preventDefault();
  var first_name = $("#firstName").val(); 
  var middle_name = $("#middleName").val();
  var last_name = $("#lastName").val();
  var father_name = $("#fatherName").val(); 
  var mother_name = $("#motherName").val();
  var gender = $("#gender").val();
  var martial_status = $("#martialStatus").val();
  var religion = $("#religion").val();
  var employee_id = $("#employeeId").val();
  var employee_designation = $("#employeeDesignation").val();
  var residential_adddress = $("#residentialAddress").val();
  var pan_number = $("#panNumber").val();
  var Passport_number = $("#passportNumber").val();
  var bank_name = $("#bankName").val();
  var branch_name = $("#branchName").val();
  var bankaccount_number = $("#bankaccountNumber").val();
  var bankifsc_code = $("#bankifscCode").val();
  var education_qualification = $("#educationQualification").val(); 
  var dataString = 'firstName='+first_name+'&middleName='+middle_name+'&lastName='+last_name+'&fatherName='+father_name+'&motherName='+mother_name+'&gender='+gender+'&martialStatus='+martial_status+'&religion='+religion+'&employeeId='+employee_id+'&employeeDesignation='+employee_designation+'&residentialAddress='+residential_adddress+'&panNumber='+pan_number+'&passportNumber='+Passport_number+'&bankName='+bank_name+'&branchName='+branch_name+'&bankaccountNumber='+bankaccount_number+'&bankifscCode='+bankifsc_code+'&educationQualification='+education_qualification;
  console.log(dataString);
  $.ajax({
    type:'POST',
    data:dataString,
    url:'http://127.0.0.1:8000/registration/',
    success:function(data) {
      alert(data);
      location.reload();
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
        tableData=tableData+'<tr><td>'+data[i].first_name+'</td><td>'+data[i].middle_name+'</td><td>'+'<tr><td>'+data[i].last_name+'</td><td>'+data[i].father_name+'</td><td>'+data[i].mother_name+'</td><td>'+data[i].gender+'</td><td>'+data[i].religion+'</td><td>'+data[i].residental_address+'</td></tr>'+'<tr><td>'+data[i].martial_status+'</td><td>'+'<tr><td>'+data[i].employee_id+'</td><td>'+'<tr><td>'+data[i].employee_designation+'</td><td>'+'<tr><td>'+data[i].pan_number+'</td><td>'+'<tr><td>'+data[i].passport_number+'</td><td>'+'<tr><td>'+data[i].bank_name+'</td><td>'+'<tr><td>'+data[i].branch_name+'</td><td>'+'<tr><td>'+data[i].bankaccount_number+'</td><td>'+'<tr><td>'+data[i].bankifsc_code+'</td><td>'+'<tr><td>'+data[i].education_qualification+'</td><td>';
      }
      $('#tbody').html(tableData);
      //alert(data);
    }
  });    
});
