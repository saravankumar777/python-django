$(function () {
    var backend_url = 'http://localhost:9000';
        $("#loginSubmit").click(function (event) {
            data = {
                'username': $.trim(document.getElementById("username").value.toLowerCase()),
                'password': document.getElementById("password").value,
            }
        console.log(data);
            if (data.username && data.password) {
                $.ajax({
                    url: backend_url + '/login/',
                    type: "POST",
                    data: data,
                    //crossDomain: true,
                    //processData: false,
                    //dataType: 'json',
                    //headers: {'content-type': 'application/json;'},
                    success: function (success) {
                        localStorage.setItem('activeUser', JSON.stringify(success.user));
                        window.location.href = "tickets.html";
                     },
                    error: function (error) {
                        console.log(error);
                        $('#error_msg').show();
                        //window.location.href = "index.html";          
            }           
            });

            }
            event.preventDefault();
        });
    });
