$(document).ready(function(){
    $('#ticketType').change(function(){
        console.log(this.value);
        var valueIndex=this.value;
        var hiddenDiv = document.getElementById(valueIndex);
        $('.tab-content').hide();
        hiddenDiv.style.display = (this.value == "") ? "none":"block";
    });
});