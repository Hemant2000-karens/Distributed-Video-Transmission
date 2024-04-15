// // Add event listener to track video playback
// document.getElementById('video-player').addEventListener('play', function() {
//     // Send AJAX request to server to update watch count
//     var xhr = new XMLHttpRequest();
//     xhr.open('POST', '/update_watch_count/', true);
//     xhr.setRequestHeader('Content-Type', 'application/json');
//     xhr.onreadystatechange = function() {
//         if (xhr.readyState === XMLHttpRequest.DONE) {
//             // Handle response from server
//             if (xhr.status === 200) {
//                 console.log('Watch count updated successfully.');
//             } else {
//                 console.error('Failed to update watch count.');
//             }
//         }
//     };
//     xhr.send(JSON.stringify({ action: 'play' }));
// });


const videoPlayer = document.getElementById('video-player');
    videoPlayer.addEventListener('play', function() {
        const videoId = '{{ broadcast_info.pk }}';
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
            } else {
                console.error('Failed to update watch count');
            }
        })
        .catch(error => console.error('Error:', error));
    });