$( document ).ready(function(){  
  $('.list').slideUp(0);
  
  $('img.logo').each(function(){    
            
    $(this).on('click', function(){
        
        var thisid = $(this).attr('id'); //logo6
        var listid = 'div#'+thisid; //div#logo6
        
        $(listid).slideToggle();      
    })
   });   
  
  $('.deleteConfirm').on('click', function(){
    return confirm('確定刪除?');
  })

  
  
  $('span#likeaccoun').each(function(){    
    var like ='/self/articleRead/'+ $(this).attr('class'); 
    $(this).load(like +' .likeshow')
   });   
  
  $('.more').each(function(){    
    
    $(this).on('click', function(){
      
      var content ='/self/articleRead/'+ $(this).attr('id'); 
      $(this).parent('.context').load(content +' .content')
    })
    
   });
  
  $('.liketest').each(function(){    
    var url ='/self/articleLike/'+ $(this).attr('id'); 
    $(this).on('click', function(){      
      $.ajax({
        url:url,
        type:"get",
        dataType:"json",
        data:{
            articleid:'{{ article.id }}'
        },
        success:function(result){
            $('#likecount').html(result.total_like_query)
        }
    })
        
    });
    
   });
  
  
  $('.likereadtest').each(function(){    
    var url ='/self/articleLike/'+ $(this).attr('id'); 
    var thisid = $(this).attr('id');
    var url2 = 'span.'+thisid;
    $(this).on('click', function(){      
      $.ajax({
        url:url,
        type:"get",
        dataType:"json",
        data:{
            articleid:'{{ article.id }}'
        },
        success:function(result){
          $(url2).html(result.total_like_query)
        }
    })
        
    });
    
   });
  
  $('.commentlist').slideUp(0);
  
  $('img.commentlogo').each(function(){    
            
    $(this).on('click', function(){
        
        var thisid = $(this).attr('id'); //commentlist6
        var listid = 'div#'+thisid; //div#commentlist6
        
        $(listid).slideToggle();      
    })
   });   
  
 
});

