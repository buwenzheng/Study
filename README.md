# PETS

### 项目目录

├── LICENSE
├── README.md
├── build
│   ├── build.js
│   ├── check-versions.js
│   ├── logo.png
│   ├── utils.js
│   ├── vue-loader.conf.js
│   ├── webpack.base.conf.js
│   ├── webpack.dev.conf.js
│   └── webpack.prod.conf.js
├── config
│   ├── dev.env.js
│   ├── index.js
│   └── prod.env.js
├── dist
│   ├── favicon.ico
│   ├── index.html
│   └── static
│       ├── css
│       │   └── app.52648b571263795b045a9161ef7a7afc.css
│       ├── fonts
│       │   ├── element-icons.535877f.woff
│       │   └── element-icons.732389d.ttf
│       ├── img
│       │   ├── bg.44145c3.jpg
│       │   ├── login-bg.ea97f22.png
│       │   ├── logo.9721a1b.png
│       │   ├── none.1e0e328.png
│       │   └── title.655b07a.png
│       └── js
├── exit
├── favicon.ico
├── index.html
├── jenkinsfile
├── package.json
├── src
│   ├── App.vue
│   ├── api
│   │   ├── common.js
│   │   └── url.js
│   ├── components
│   │   ├── dialog
│   │   │   └── comfirm-remove.vue
│   │   ├── month-picker
│   │   │   └── index.vue
│   │   ├── new-month-picker
│   │   │   └── index.vue
│   │   ├── pages
│   │   │   └── index.vue
│   │   ├── range-date-picker
│   │   │   └── index.vue
│   │   ├── scroll-bar
│   │   │   └── index.vue
│   │   ├── svg-icon
│   │   │   └── index.vue
│   │   ├── week-picker
│   │   │   └── index.vue
│   │   └── year-picker
│   │       └── index.vue
│   ├── config
│   │   └── index.js
│   ├── icons
│   │   ├── edit.png
│   │   ├── index.js
│   │   └── svg
│   │       ├── 404.svg
│   │       ├── 500.svg
│   │       ├── add.svg
│   │       ├── back.svg
│   │       ├── circle-norm.svg
│   │       ├── circle-sero.svg
│   │       ├── circle-warn.svg
│   │       ├── circle-well.svg
│   │       ├── close.svg
│   │       ├── cup.svg
│   │       ├── delete.svg
│   │       ├── down.svg
│   │       ├── down2.svg
│   │       ├── download.svg
│   │       ├── edit.svg
│   │       ├── edit02.svg
│   │       ├── err.svg
│   │       ├── export.svg
│   │       ├── help.svg
│   │       ├── icon-calendar.svg
│   │       ├── icon-chart.svg
│   │       ├── icon-home.svg
│   │       ├── icon-portal.svg
│   │       ├── icon-project.svg
│   │       ├── icon-setting.svg
│   │       ├── icon-tip.svg
│   │       ├── import.svg
│   │       ├── login-pwd.svg
│   │       ├── login-user.svg
│   │       ├── logo.svg
│   │       ├── nav-hide.svg
│   │       ├── nav-show.svg
│   │       ├── next.svg
│   │       ├── notice.svg
│   │       ├── prev.svg
│   │       ├── proportion.svg
│   │       ├── question.svg
│   │       ├── save.svg
│   │       ├── search.svg
│   │       ├── selected.svg
│   │       ├── settings.svg
│   │       ├── succeed.svg
│   │       ├── tree-organi.svg
│   │       ├── up.svg
│   │       ├── up2.svg
│   │       └── wrong.svg
│   ├── main.js
│   ├── router
│   │   ├── index.js
│   │   └── keepAliveConfig.js
│   ├── store
│   │   ├── index.js
│   │   └── path.js
│   ├── styles
│   │   ├── element-ui.scss
│   │   ├── index.scss
│   │   ├── sidebar.scss
│   │   ├── table.scss
│   │   └── transition.scss
│   ├── utils
│   │   ├── auth.js
│   │   ├── index.js
│   │   ├── request.js
│   │   ├── validate.js
│   │   └── verify.js
│   └── views
│       ├── error
│       │   ├── 404.vue
│       │   └── 500.vue
│       ├── index
│       │   ├── dashboard.vue
│       │   ├── images
│       │   │   ├── bg.jpg
│       │   │   ├── logo.png
│       │   │   ├── none.png
│       │   │   ├── title.png
│       │   │   └── zzb.png
│       │   └── receive-token.vue
│       ├── layout
│       │   ├── components
│       │   │   ├── app-main.vue
│       │   │   ├── header.vue
│       │   │   ├── index.js
│       │   │   ├── logo.png
│       │   │   ├── nav-bar.vue
│       │   │   └── sidebar
│       │   │       ├── index.vue
│       │   │       ├── pets.png
│       │   │       └── sidebar-item.vue
│       │   └── layout.vue
│       ├── portal
│       │   ├── product-portal.vue
│       │   └── project-portal.vue
│       ├── project
│       │   ├── components
│       │   │   ├── account.vue
│       │   │   ├── add-cost-dialog.vue
│       │   │   ├── add-server-dialog.vue
│       │   │   ├── base-server.vue
│       │   │   ├── config.js
│       │   │   ├── cost-detail-dialog.vue
│       │   │   ├── count.vue
│       │   │   ├── itemInfo.scss
│       │   │   ├── itemInfo.vue
│       │   │   ├── personal-ass.vue
│       │   │   ├── quotation.vue
│       │   │   └── task.vue
│       │   ├── list.vue
│       │   └── project-desc.vue
│       ├── reportingSystem
│       │   ├── components
│       │   │   ├── dept-select.vue
│       │   │   ├── fillDetailPopup.vue
│       │   │   └── people-select.vue
│       │   ├── personal-cost-analysis.vue
│       │   ├── project-cost-analysis.vue
│       │   ├── projectAccounting.vue
│       │   ├── timeSheetPersonalInput.vue
│       │   ├── timeSheetSystem.vue
│       │   ├── vacancy-rate.vue
│       │   ├── wordTimeQuery.vue
│       │   └── workTimeSystem.vue
│       ├── systemSettings
│       │   ├── components
│       │   │   ├── customerInfoEdit.vue
│       │   │   ├── people-set-popup.vue
│       │   │   ├── portal-set-menu.vue
│       │   │   └── public-cost-menu.vue
│       │   ├── customer-info.vue
│       │   ├── function-set.vue
│       │   ├── holiday-management.vue
│       │   ├── limit-menu.vue
│       │   ├── manager-public-cost.vue
│       │   ├── menu-set.vue
│       │   ├── people-rate.vue
│       │   ├── portal-last-review.vue
│       │   ├── portal-pipeline.vue
│       │   ├── portal-point-set.vue
│       │   ├── portal-product-set.vue
│       │   ├── portal-product.vue
│       │   ├── portal-set.vue
│       │   ├── project-roles.vue
│       │   ├── rate-menu.vue
│       │   ├── rate.vue
│       │   ├── report-param-set.vue
│       │   ├── role-set.vue
│       │   ├── seat-public-cost.vue
│       │   ├── service-tariffing.vue
│       │   ├── staff-rate.vue
│       │   ├── timesheet-set.vue
│       │   ├── type-service.vue
│       │   ├── user-set.vue
│       │   └── white-list.vue
│       ├── timesheet
│       │   ├── approval.vue
│       │   ├── components
│       │   │   ├── cascader.vue
│       │   │   ├── multiple.vue
│       │   │   └── quickPicker.vue
│       │   ├── count.vue
│       │   ├── examine.vue
│       │   ├── fill-in.vue
│       │   ├── images
│       │   │   └── none.png
│       │   └── particulars.vue
│       └── user
│           ├── images
│           │   └── login-bg.png
│           └── login.vue
├── static
└── tree.txt

