document.onload = function() {
    let listNode = document.querySelectorAll('.list_item');
    listNode.forEach(node => {
        node.onclick = function() {
            // $(this).siblings().removeClass('selected');
            // $(this).addClass('selected');
            $(this).children('.children').css({display: 'block'});
            let name = $(this).attr('name'),
            index = $(this).attr('index');
            let _self = $(this);
            $.ajax({
                method: 'POST',
                url:'/list',
                data: {name, index},
                success: (res) => {
                    document.body.innerHTML = "";
                    document.write(res);
                },
                error: err => {
                    console.log(err);
                }
            })
            
        }
    })
}()