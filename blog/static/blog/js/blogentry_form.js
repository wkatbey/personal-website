var app = new Vue({
    el: '#sb-blog-form',
    data: {
        category: '',
        title: '',
        text_entry: '',
    },
    methods: {
        submitForm: function() {
            console.log(this.title);
        }
    },
    mounted() {
        this.category = '';
        this.title = '';
        this.text_entry = '';
    }
})
