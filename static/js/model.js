
$("body").on('click', function() {
    $("#mensagem").remove()
})


new DataTable('#myTable', {
    layout: {
        topStart: {
            buttons: ['copyHtml5', 'excelHtml5', 'csvHtml5', 'pdfHtml5']
        }
    },

    "columnDefs": [
        {"className": "dt-center", "targets": "_all"}
      ],
});

$("#importArq").on('click', function(){
    $( ".selector" ).dialog({
        width: 400,
        height: 200
      });
})
