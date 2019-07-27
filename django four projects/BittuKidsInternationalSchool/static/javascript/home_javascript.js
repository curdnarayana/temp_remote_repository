 var images=[
               "Awards.png",
			   "Capture.png",
			   "Awards.png",
			   "download2.jpg",
			   "principal.png",
			   "principal1.png"
              ];
    var i=0;
	function slides()
	{
	  document.getElementById("slideimage").src=images[i];
	  if (i<(images.length-1))
	  {
		  i++;
	  }
	  else
	   i=0;
    }
	setInterval(slides,2000)
   }