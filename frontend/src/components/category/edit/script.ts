import Vue from 'vue';
import Category from '@/entity/category';


export default Vue.extend({
    props: {
        category: {
            required: true
        }
    },
    data() {
        return {
            error: false
        };
    },
    computed: {
        hasError(): boolean {
            return this.error;
        }
    },
    methods: {
        handleSave(): void {
            //this.hasError = this.category.name === '';
            //console.log('run');
            this.$emit('save-successfully');
        }
    }
});

