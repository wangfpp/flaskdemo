document.onload = function() {
    console.log(111)
    $('#uploadfile').change(function(e) {
        let files = e.target.files;
        console.log(files)
        let formdata = new FormData();
        for(var i = 0; i < files.length; i++) {
            formdata.append(files[i].name, files[i]);
        }
        $.ajax({
            method: 'POST',
            url: '/upload',
            processData: false,
            contentType : false,
            data: formdata,
            dataType: 'json',
            success: res => {
                console.log(res);
            },
            error: err => {
                console.log(err);
            }
        })
    })
}()