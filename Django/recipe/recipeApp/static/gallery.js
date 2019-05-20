var gallery = new Vue({
	el: '#gallery',
	data: {
		Recipes: [],
		seen:true,
		unseen:false
	},
	created: function() {
		this.fetchRecipes();
		this.timer = setInterval(this.fetchRecipes, 10000);
	},
	methods: {
		fetchRecipes: function() {
			axios
				.get('/galleryitems')
				.then(response => (this.Recipes = response.data.Recipes))
			console.log(this.Recipes)
			this.seen = false
			this.unseen = true
		},
		cancelautoupdate: function() { clearInterval(this.timer) }
	},
	beforeDestroy() {
		clearInterval(this.timer)
	}
})
