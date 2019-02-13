import Vue from 'vue';
import moment from 'moment';


// mock
function getItems() {
    return [
        [
            { sales_date: null, amount: null, is_holiday: false, is_satarday: false},
            { sales_date: null, amount: null, is_holiday: false, is_satarday: false},
            { sales_date: null, amount: null, is_holiday: false, is_satarday: false},
            { sales_date: null, amount: null, is_holiday: false, is_satarday: false},
            { sales_date: 1, amount: 100000, is_holiday: false, is_satarday: false},
            { sales_date: 2, amount: 100000, is_holiday: false, is_satarday: false},
            { sales_date: 3, amount: 100000, is_holiday: true, is_satarday: false}
        ],
        [
            { sales_date: 4, amount: 100000, is_holiday: true, is_satarday: false},
            { sales_date: 5, amount: 100000, is_holiday: false, is_satarday: false},
            { sales_date: 6, amount: 100000, is_holiday: false, is_satarday: false},
            { sales_date: 7, amount: 100000, is_holiday: false, is_satarday: false},
            { sales_date: 8, amount: 100000, is_holiday: false, is_satarday: false},
            { sales_date: 9, amount: 100000, is_holiday: false, is_satarday: false},
            { sales_date: 10, amount: 100000, is_holiday: false, is_satarday: true}
        ],
        [
            { sales_date: 11, amount: 100000, is_holiday: true, is_satarday: false},
            { sales_date: 12, amount: 100000, is_holiday: false, is_satarday: false},
            { sales_date: 13, amount: 100000, is_holiday: false, is_satarday: false},
            { sales_date: 14, amount: 100000, is_holiday: false, is_satarday: false},
            { sales_date: 15, amount: 100000, is_holiday: false, is_satarday: false},
            { sales_date: 16, amount: 100000, is_holiday: false, is_satarday: false},
            { sales_date: 17, amount: 100000, is_holiday: false, is_satarday: true},
        ],
        [
            { sales_date: 18, amount: 100000, is_holiday: true, is_satarday: false},
            { sales_date: 19, amount: 100000, is_holiday: false, is_satarday: false},
            { sales_date: 20, amount: 100000, is_holiday: false, is_satarday: false},
            { sales_date: 21, amount: 100000, is_holiday: false, is_satarday: false},
            { sales_date: 22, amount: 100000, is_holiday: false, is_satarday: false},
            { sales_date: 23, amount: 100000, is_holiday: false, is_satarday: false},
            { sales_date: 24, amount: 100000, is_holiday: false, is_satarday: true},
        ],
        [
            { sales_date: 25, amount: 100000, is_holiday: true, is_satarday: false},
            { sales_date: 26, amount: 100000, is_holiday: false, is_satarday: false},
            { sales_date: 27, amount: 100000, is_holiday: false, is_satarday: false},
            { sales_date: 28, amount: 100000, is_holiday: false, is_satarday: false},
            { sales_date: 29, amount: 100000, is_holiday: false, is_satarday: false},
            { sales_date: 30, amount: 100000, is_holiday: false, is_satarday: false},
            { sales_date: null, amount: null, is_holiday: false, is_satarday: false}
        ]
    ];
}

export default Vue.extend({
    data() {
        const monthlySales = getItems();
        const popularItems = [
            {'rank': 1, 'item': 'Gamoyonカレー'},
            {'rank': 2, 'item': 'Siphonコーヒー'},
            {'rank': 3, 'item': 'ペペロンチーノ'},
            {'rank': 4, 'item': 'ガトーショコラ'},
            {'rank': 5, 'item': '究極のチーズケーキ'},
            {'rank': 6, 'item': 'Gamoyonカレー'},
            {'rank': 7, 'item': 'Siphonコーヒー'},
            {'rank': 8, 'item': 'ペペロンチーノ'},
            {'rank': 9, 'item': 'ガトーショコラ'},
            {'rank': 10, 'item': '究極のチーズケーキ'}
        ];
        const today = moment().toDate();

        return {
            popularItems,
            monthlySales,
            today
        };
    },
    computed: {
        currentMonth(): string {
            return moment(this.today).format('YYYY年MM月');
        }
    },
    methods: {
        handlePrevMonth(): void {
            this.today = moment(this.today).add(-1, 'M').toDate();
        },
        handleNextMonth(): void {
            this.today = moment(this.today, 'YYYY-MM-DD').add(1, 'M').toDate();
        }
    },
    filters: {
        numberWithDelimiter(value: number): string {
            if (!value) {
                return '';
            }
            return value.toString().replace(/(\d)(?=(\d{3})+$)/g, '$1,');
        }
    }
});

