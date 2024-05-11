$(document).ready(function () {
  console.log("Rehan Nagoor Mohideen  1100592");

  $("#getNews").click(function () {
    $.ajax({
      url: "/getnews",
      success: function (result) {
        var el = $("<div></div>");
        el.html(result);
        // console.log(result);
        var parsedResult = $("li", el).slice(9, 19);
        $(".source3").html(parsedResult);
      },
    });
  });
});
