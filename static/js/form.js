//autocomplete profissao para teste
$.ajax({
    url: "/buscaProfissao",
    method: "GET",

    success: function(data){
        lista = $.map(data,function(valor, index){
            //obtem o primeiro e unico valor retornado da rota
            return valor[0]  
        })

        $( "#prof" ).autocomplete({
            source: lista
        });
    }

})
    

