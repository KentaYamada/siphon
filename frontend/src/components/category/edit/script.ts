import Vue from 'vue';
import _ from 'lodash';
import Category from '@/entity/category';
import CategoryService from '@/api/category.service';

export default Vue.extend({
    props: {
        category: {
            required: true,
            type: Category
        }
    },
    data() {
        return {
            errors: {}
        };
    },
    
    methods: {
        /**
         * 保存イベント
         */
        handleSave(): void {
            CategoryService.saveCategory(this.category)
                .then((response: any) => {
                    this.$emit('close');
                    this.$emit('save-success', response.data.message);
                })
                .catch((error: any) => {
                    const response = error.response;
                    this.$toast.open({
                        message: response.data.message,
                        type: 'is-danger'
                    });

                    if (!_.isEmpty(response.data.errors)) {
                        this.errors =  _.extend({}, response.data.errors);
                    }
            });
        }
    }
});

