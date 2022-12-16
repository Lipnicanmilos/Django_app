function getCities(season_name_id){
    let $ = django.jQuery;
    $.get("/blog/Team_home/list/" + season_name_id, function(response){
        
        let teams = '<option value="">---------------</option>';
        $.each(response.data, function(i, Team_home){
            teams += '<option value="' + Team_home.id + '">' + Team_home.name + '</option>'
        });

        $("#id_Team_home").html(teams);

        let teamv = '<option value="">---------------</option>';
        $.each(response.data, function(i, Team_visitor){
            teamv += '<option value="' + Team_visitor.id + '">' + Team_visitor.name + '</option>'
        });

        $("#id_Team_visitor").html(teamv);
    })
}