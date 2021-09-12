(function ($) {
  function wookit_functions(){
    
    
    function wookit_stars_wrapper(){
      $('.woocommerce ul.products li.product .star-rating').wrap('<div class="star-rating-wrapper"></div>');
      $('.woocommerce ul.products li.product .star-rating').css({opacity: 1});
    }
    
    function wookit_order_title_fix(){
      $('h3#order_review_heading').wrapInner('<div class="order_review_heading_inner"></div>');
      $('h3#order_review_heading').css({opacity: 1});

    }
    
    
    
    
    
    
    return {
      wookit_stars_wrapper: wookit_stars_wrapper,
      wookit_order_title_fix: wookit_order_title_fix,
    }; 
  }
  
  

$(document).ready(function(){
  wookit_functions().wookit_stars_wrapper();
  wookit_functions().wookit_order_title_fix();
})
  
  
}(jQuery));