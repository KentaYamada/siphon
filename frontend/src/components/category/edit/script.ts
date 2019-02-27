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
            errors: {}
        };
    },
    methods: {
        handleSave(): void {
            this.$emit('save-success');
        }
    }
});

