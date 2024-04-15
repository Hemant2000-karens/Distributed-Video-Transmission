var videoPlayer = document.getElementById("video-player");
var hasUpdated = false; // Variable to track whether the view count has been updated
var csrftoken = document.getElementById("csrf-token").value;


videoPlayer.addEventListener('play', function() {
    if (!hasUpdated) {
        const videoId = videoPlayer.dataset.videoId;
        fetch('/update_watch_count/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}'
            },
            body: JSON.stringify({
                action: 'play',
                video_id: videoId
            })
        })
        .then(response => {
            if (response.ok) {
                console.log('Watch count updated successfully');
                hasUpdated = true; // Set to true to prevent further updates
            } else {
                console.error('Failed to update watch count');
            }
        })
        .catch(error => console.error('Error:', error));
    }
});

videoPlayer.addEventListener('pause', function() {
    if (!hasUpdated) {
        const videoId = videoPlayer.dataset.videoId;
        fetch('/update_watch_count/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}'
            },
            body: JSON.stringify({
                action: 'pause',
                video_id: videoId
            })
        })
        .then(response => {
            if (response.ok) {
                console.log('Watch count updated successfully');
                hasUpdated = true; // Set to true to prevent further updates
            } else {
                console.error('Failed to update watch count');
            }
        })
        .catch(error => console.error('Error:', error));
    }
});



const videoId = videoPlayer.dataset.videoId;
    console.log('Video ID:', videoId);
