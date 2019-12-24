document.onload = function() {
    $('#uploadfile').change(function(e) {
        let files = e.target.files;
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
            xhr: function() { //原声的AJAX的文件上传进度事件
                var myxhr = $.ajaxSettings.xhr();
                console.log(myxhr)
                if (myxhr.upload) {
                    myxhr.upload.addEventListener('progress', onprogress, false);
                }
                return myxhr;
            },
            success: res => {
                console.log(res);
            },
            error: err => {
                console.log(err);
            }
        })
    })
    function onprogress(e) {
        if (e.lengthComputable) {
            let percent = parseInt((e.loaded / e.total) * 100)
            let total =  (100 - percent - 10) / 100
            $('input').css({'background-image': `linear-gradient(to right,  #52c41a ${percent}%, #f5f5f5 ${total}%)`})
        }
    }
}()