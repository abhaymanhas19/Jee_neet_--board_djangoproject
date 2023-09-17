// testinomial 

function testiminialImagesSet() {
	setTimeout(() => {
		let images = [];
		var paginateLt = $('.owl-pagination').children(".owl-page").length;
		$("#testimonial-slider .owl-item").each(function () {
			var srcData = $(this).find('.testimonial').attr('data-image');
			images.push(srcData);
		})
		if (images.length === paginateLt) {
			let imgCount = 0;
			$('.owl-pagination .owl-page').each(function () {
				$(this).find("span").css('background-image', `url(${images[imgCount]})`);
				imgCount = imgCount + 1;
			})
		}
		console.log("Images set");
	}, 1000);

}
$(document).ready(function () {
	$("#testimonial-slider").owlCarousel({
		items: 1,
		itemsDesktop: [1000, 1],
		itemsDesktopSmall: [979, 1],
		itemsTablet: [768, 1],
		pagination: true,
		navigation: true,
		navigationText: ["", ""],
		slideSpeed: 1000,
		autoPlay: true
	});
	setTimeout(() => {
		testiminialImagesSet();
	}, 1000);
	$(window).resize(function () {
		testiminialImagesSet();
	});
});
jQuery(document).ready(function($) {
	$('a[href^="#"]').bind('click.smoothscroll',function (e) {
	  e.preventDefault();
	  var target = this.hash,
		  $target = $(target);
	  $('html, body').stop().animate( {
		'scrollTop': $target.offset().top-80
	  }, 400,function () {
		window.location.hash = target;
	  } );
	} );
  } );

// counter

(function ($) {
	$.fn.countTo = function (options) {
		options = options || {};
		
		return $(this).each(function () {
			// set options for current element
			var settings = $.extend({}, $.fn.countTo.defaults, {
				from:            $(this).data('from'),
				to:              $(this).data('to'),
				speed:           $(this).data('speed'),
				refreshInterval: $(this).data('refresh-interval'),
				decimals:        $(this).data('decimals')
			}, options);
			
			// how many times to update the value, and how much to increment the value on each update
			var loops = Math.ceil(settings.speed / settings.refreshInterval),
				increment = (settings.to - settings.from) / loops;
			
			// references & variables that will change with each update
			var self = this,
				$self = $(this),
				loopCount = 0,
				value = settings.from,
				data = $self.data('countTo') || {};
			
			$self.data('countTo', data);
			
			// if an existing interval can be found, clear it first
			if (data.interval) {
				clearInterval(data.interval);
			}
			data.interval = setInterval(updateTimer, settings.refreshInterval);
			
			// initialize the element with the starting value
			render(value);
			
			function updateTimer() {
				value += increment;
				loopCount++;
				
				render(value);
				
				if (typeof(settings.onUpdate) == 'function') {
					settings.onUpdate.call(self, value);
				}
				
				if (loopCount >= loops) {
					// remove the interval
					$self.removeData('countTo');
					clearInterval(data.interval);
					value = settings.to;
					
					if (typeof(settings.onComplete) == 'function') {
						settings.onComplete.call(self, value);
					}
				}
			}
			
			function render(value) {
				var formattedValue = settings.formatter.call(self, value, settings);
				$self.html(formattedValue);
			}
		});
	};
	
	$.fn.countTo.defaults = {
		from: 0,               // the number the element should start at
		to: 0,                 // the number the element should end at
		speed: 1000,           // how long it should take to count between the target numbers
		refreshInterval: 100,  // how often the element should be updated
		decimals: 0,           // the number of decimal places to show
		formatter: formatter,  // handler for formatting the value before rendering
		onUpdate: null,        // callback method for every time the element is updated
		onComplete: null       // callback method for when the element finishes updating
	};
	
	function formatter(value, settings) {
		return value.toFixed(settings.decimals);
	}
}(jQuery));

jQuery(function ($) {
  // custom formatting example
  $('.count-number').data('countToOptions', {
	formatter: function (value, options) {
	  return value.toFixed(options.decimals).replace(/\B(?=(?:\d{3})+(?!\d))/g, ',');
	}
  });
  
  // start all the timers
  $('.timer').each(count);  
  
  function count(options) {
	var $this = $(this);
	options = $.extend({}, options || {}, $this.data('countToOptions') || {});
	$this.countTo(options);
  }
});

// image slider


 
$(document).ready(function(){
    $("#image-slider").owlCarousel({
        items:4,
        itemsDesktop:[1000,1],
        itemsDesktopSmall:[979,2],
        itemsTablet:[768, 2],
        pagination:false,
        navigation:true,
        navigationText:["",""],
        slideSpeed:1000,
        autoPlay:true
    });
});


//video slider


$(document).ready(function () {
    $("#video-slider").owlCarousel({
        items: 4,
        itemsDesktop: [1000, 1],
        itemsDesktopSmall: [979, 2],
        itemsTablet: [768, 2],
        pagination: false,
        navigation: true,
        navigationText: ["", ""],
        slideSpeed: 1000,
        autoPlay: true,
    });
});