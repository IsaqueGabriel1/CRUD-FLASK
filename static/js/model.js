
//mensagem de retorno do servidor
$("body").on('click', function() {
    $("#mensagem").remove()
})

//inicia a tabela com os botões de excel, copia, csv e pdf no começo do topo
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

//importação de dados em massa
$("#importArq").on('click', function(){
    $( ".selector" ).dialog({
        width: 400,
        height: 200
      });
})



