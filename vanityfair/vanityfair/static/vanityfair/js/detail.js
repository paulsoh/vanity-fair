(function(){
    
    $(document).ready(function(){
        var comment_element = $("#comment");
        var post_id = comment_element.data("post-id");
        $.ajax({
            url: "/api/posts/" + post_id + "/comments/",
            type: "GET",
            success: function(comments){
                console.log(comments);
                for(var i = 0; i < comments.length; i++) {
                    var comment = comments[i];
                    console.log(comment.content);
                    comment_element.append(
                        "<p>"+comment.content+
                        " by "+comment.user+
                        "</p>"
                    );
                }
            }
        });

		function getCookie(name) {
			var cookieValue = null;
			if (document.cookie && document.cookie != '') {
				var cookies = document.cookie.split(';');
				for (var i = 0; i < cookies.length; i++) {
					var cookie = jQuery.trim(cookies[i]);
					// Does this cookie string begin with the name we want?
					if (cookie.substring(0, name.length + 1) == (name + '=')) {
						cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
						break;
					}
				}
			}
			return cookieValue;
		}

        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }
        
		var csrftoken = getCookie('csrftoken');

        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });


        var $submit = $("#submit");
        var $comment = $("textarea#comment");
        
        console.log(csrftoken)

        $submit.click(function(){
            console.log($comment.val());
            $.ajax({
                url: "/api/posts/" + post_id + "/comments/",
                type: "POST",
                data: {
                    "content": $comment.val(),
                    "post": post_id
                }
            })
            .done(function(data, textStatus, jqXHR){
                console.log("Http request suceeded: "+jqXHR.status);
            })
            .fail(function(jqXHR, textStatus, errorThrown){
                console.log("Http request suceeded: "+jqXHR.status);
                console.log(textStatus);
                console.log(errorThrown);
            })
        });
    });

})();
