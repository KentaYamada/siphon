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
            errors: {
                //name: 'カテゴリ名は必須です'
            }
        };
    },
    computed: {
    },
    methods: {
        handleSave(): void {
            //this.hasError = this.category.name === '';
            //console.log('run');
            this.$emit('save-successfully');
        }
    }
});

