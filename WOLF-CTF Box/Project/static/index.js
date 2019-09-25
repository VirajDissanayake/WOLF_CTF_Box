$(document).ready(function() {

   var totalTime = 7200; // Amout of time (sec)
   var halfTime = Math.floor(totalTime / 2);

   if (!Cookies.get('cdTime')) {
      var now = $.now(); // First time on page
      Cookies.set('firstTime', now, {
         expires: 7,
         path: '/'
      });
      Cookies.set('cdTime', totalTime, {
         expires: 7,
         path: '/'
      });
      var runTimer = Cookies.get('cdTime');
   } else {
      var currentTime = $.now();
      var usedTime = (currentTime - Cookies.get('firstTime')) / 1000; // Calculate and convert into seconds
      var runTimer = Cookies.get('cdTime') - usedTime;
   }
   $('#cd').countdown({
      until: runTimer,
      compact: true,
      onExpiry: EndCountdown,
      onTick: Callbacks,
      layout: 'Total time left - {hn} hour {mn} minutes and {sn} seconds'
   });

   function Callbacks(periods) {
      if ($.countdown.periodsToSeconds(periods) === halfTime) {
         $('#cd').addClass('halfway');
      }
      else if ($.countdown.periodsToSeconds(periods) <= 0) {
         EndCountdown();
      }
   }

   function EndCountdown() {
      $('#cd').removeClass('halfway').addClass('ended');
      $('#cd').html('Expired!');
   }

});
