function ajax(type, url, data, success, error) {
    $.ajax({
        method: type || 'GET',
        url: url,
        data: data,
        success: success(res),
        error: error(err)
    })
}