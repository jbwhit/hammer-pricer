function queryURL(query) {
    $("#query").val(query);
    visualize();        
}

function visualize() {
    var url = "/analyze";
    var Q = $("#query").val();
    var html = '<img src="static/img/ajaxSpinner.gif" alt="Please wait" width=40px height=40px>';
    $("#spinner").html(html);    
    $("#google-table" ).empty();
    $("#people-info" ).empty();
    $.post(url, {'jobQuery':Q}, cback); 
}

function drawd3(results) {
    // Try CSV first
    d3.csv("../static/data/")

}

function cback(results) {
    window.history.pushState("", "InvestWiser", "/fetchcompany?q="+results['query']);

    $("#spinner").html('');
    $("#timelinebut").css("background", "#FFCC66");
    $("#timelinebut").css("color", "#fff");
    $("#timelinebut").css("border", "0px");

    appendFounderImg(results);
}

function appendFounderImg(data) {
   $('#people-info').prepend('<img alt="" src="' + data['company_img'] + ">'");
}
