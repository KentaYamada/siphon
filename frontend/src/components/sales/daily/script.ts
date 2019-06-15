import Vue from 'vue';
import {
    mapActions,
    mapGetters
} from 'vuex';
import moment from 'moment';
import _ from 'lodash';
import DailySalesItem from '@/components/sales/daily/item/DailySalesItem.vue';
import { DailySalesSearchOption } from '@/entity/daily_sales';


/**
 * 日次売上一覧
 */
export default Vue.extend({
    data() {
        const option: DailySalesSearchOption = {
            sales_date: '',
            time_from: '',
            time_to: '',
            q: ''
        };

        const params = this.$route.query;
        option.sales_date = params.sales_date as string;

        return {
            option
        };
    },
    mounted() {
        this.fetchDailySales(this.option);
    },
    components: {
        DailySalesItem
    },
    computed: {
        title(): string {
            return `${moment().format('YYYY年MM月DD日')}の売上`;
        },
        ...mapGetters('daily_sales', [
            'getDailySales',
            'hasItems'
        ])
    },
    methods: {
        /**
         * 売上検索
         */
        handleSearch(): void {
            this.fetchDailySales(this.option);
        },
        /**
         * 検索条件クリア
         */
        handleClearConditions(): void {
            this.$data.option.sales_date = null;
            this.$data.option.time_from = '';
            this.$data.option.time_to = '';
            this.$data.option.q = '';
        },
        ...mapActions('daily_sales', [
            'fetchDailySales'
        ])
    }
});
