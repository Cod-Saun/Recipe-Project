var app = new Vue({
	el: '#app',
	data: {
		Playlist: [],
		seen:true,
		unseen:false
	},

	created: function() {
		this.fetchPlaylist();
		this.timer = setInterval(this.fetchPlaylist, 10000);
	},
	methods: {
		fetchPlaylist: function() {
			axios
				.get('/playlist')
				.then(response => (this.Playlist = response.data.Playlist))
			this.seen=false
			this.unseen=true
		},
		cancelAutoUpdate: function() { clearInterval(this.timer) }
	},
	beforeDestroy() {
		clearInterval(this.timer)
	}
})
