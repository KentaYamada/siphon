import Vue from 'vue';
import Category from '@/entity/category';


export default Vue.extend({
    props: {
    },
    data() {
        const categories = Category.getDummyCategories();

        return {
            categories
        };
    },
    methods: {
        handleSave(): void {
            this.$emit('save-saccess');
        }
    }
});
