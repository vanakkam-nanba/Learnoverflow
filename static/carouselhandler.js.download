jQuery(function($){

$(document).ready(function(){
 
  
  function wookit_carousel_singleproduct(){
    var wrapper = $('.wookit-carousel-outer-wrapper');
    var carousel = $('.wookit-carousel-wrapper');
    var $position = 'wookit_after_single_product';
    var $dataposition = carousel.attr('data-position');
    if($dataposition != '') { $position = $dataposition;}
    var $columns = carousel.attr('data-columns');
    var $slidestoscroll = carousel.attr('data-slides');
    var $autoplay = carousel.attr('data-autoplay'); if($autoplay == 'false'){$autoplay = 0;}else {$autoplay = 1;}
    var $speed = carousel.attr('data-speed');
    var $arrows = carousel.attr('data-arrows'); if($arrows == 'false'){$arrows = 0;}else {$arrows = 1;}
    var $dots = carousel.attr('data-dots'); if($dots == 'false'){$dots = 0;}else {$dots = 1;}
    var $displaytitle = carousel.attr('data-title');
    var $displayprice = carousel.attr('data-price');
    var $displaybutton = carousel.attr('data-button');
    
    wrapper.find('li.product').css({clear: 'none'});
    wrapper.find('li.product').wrapInner('<div class="wookit-product-inner-wrapper"></div>');
    wrapper.find('li a.button').wrap('<div class="wookit-button-outer-wrapper"></div>');
    wrapper.appendTo('.'+$position);
    
    if($displaytitle == 'false'){
       carousel.find('.woocommerce-loop-product__title').remove();
    }
    
    if($displayprice == 'false'){
       carousel.find('span.price').remove();
    }
    
    if($displaybutton == 'false'){
       carousel.find('.wookit-button-outer-wrapper').remove();
    }
    
    
    carousel.find('ul.products').slick({
     // prevArrow:$previous,
      //nextArrow:$next,
      infinite: true,
      slidesToShow: parseInt($columns),
      slidesToScroll: parseInt($slidestoscroll),
      arrows: Boolean($arrows),
      autoplay: Boolean($autoplay),
      dots: Boolean($dots),
      autoplaySpeed: $speed,
      zIndex: 90,
      responsive: [
        {
          breakpoint: 980,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1,
          }
        },
        {
          breakpoint: 767,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1,
          }
        },
      ]
    });
  wrapper.css({opacity: 1});
  
    
    
  } // wookit_carousel_singleproduct
  wookit_carousel_singleproduct();
  

  
});  // $(document).ready
  
  
}) // jQuery(function($)