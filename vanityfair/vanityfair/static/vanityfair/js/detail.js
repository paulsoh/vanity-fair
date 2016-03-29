(function(){
    
    $(document).ready(function(){
        var comment_element = $("#comment");
        var post_id = comment_element.data("post-id");

        $.ajax({
            url: "/api/posts/" + post_id + "/comments/",
            type: "GET",
            success: function(comment){
                for(var i=0; i<comment.length; i++){
                    var comment = comment[i];
                    comment_element.append(
                        "<p>"+comment.content+
                        " by "+comment.user+
                        "</p>"
                    );
                }
            }
        });
    });
})();
