import xadmin

# 全局配置
from xadmin import views

from apps.main.models import Navigation, Shop, User, Image, Review, Banner, Category, Order, Property, PropertyValue, \
    ShopCar, SubMenu, SubMenu2


class BaseStyleSettings:
    # 开启主题修改
    enable_themes = True
    # 使用bootbootstrap的主题
    use_bootswatch = True


# 注册自定义全局配置
xadmin.site.register(views.BaseAdminView,BaseStyleSettings)


class GlobslSettings:
    # 修改标题
    site_title = '91商城后台管理'
    # 修改底部显示
    site_footer = '91科技有限公司,用技术填充你的空虚!'


# 注册自定义全局配置
xadmin.site.register(views.CommAdminView, GlobslSettings)

class NavigationAdmin:
    #默认情况下显示object对象
    list_display=['nav_id','nav_name']

xadmin.site.register(Navigation,NavigationAdmin)


class ShopAdmin:
    list_display=['shop_id','name','sub_title','create_date','original_price','promote_price','stock','cate']
    #修改默认分页的条数
    list_per_page = 10
    #搜索字段
    search_fields =['name','sub_title']
    list_editor =[]
xadmin.site.register(Shop,ShopAdmin)


#自定义xadmin
from xadmin.plugins import auth

#显示自定义的方式
class UserAdmin(auth.UserAdmin):
    list_display = ['id','username','email','img_show']
#先注销
xadmin.site.unregister(User)

#在注册
xadmin.site.register(User,UserAdmin)



class ImageAdimn:
    list_display=['shop_img_id','shop','type']
    list_per_page = 10
    # 搜索字段
    search_fields = ['type']
xadmin.site.register(Image,ImageAdimn)


class ReviewAdmin:
    list_display =['review_id','content','create_date','shop','user']
    list_per_page = 10
    # 搜索字段
    search_fields = ['shop','content']

xadmin.site.register(Review, ReviewAdmin)



class BannerAdmin:
    list_display = ['banner_id', 'title', 'image', 'detail_url', 'order','create_time']
    list_per_page = 10
    # 搜索字段
    search_fields = ['title']

xadmin.site.register(Banner, BannerAdmin)

class CategoryAdmin:
    list_display = ['cate_id', 'name']
    list_per_page = 10
    # 搜索字段
    search_fields = ['name']

xadmin.site.register(Category, CategoryAdmin)

class OrderAdmin:
    list_display =['oid','order_code','address','post','receiver','mobile','user_message','create_date','pay_date','delivery_date','confirm_date','status','user']
    list_per_page = 10
    # 搜索字段
    search_fields = ['user','oid']

xadmin.site.register(Order,OrderAdmin)


class PropertyAdmin:
    list_display =['property_id','name','cate']
    list_per_page = 10
    # 搜索字段
    search_fields = ['name']

xadmin.site.register(Property,PropertyAdmin)

class PropertyValueAdmin:
    list_display = ['pro_value_id', 'shop', 'property','value']
    list_per_page = 10
    # 搜索字段
    search_fields = ['shop']

xadmin.site.register(PropertyValue, PropertyValueAdmin)


class ShopCarAdmin:
    list_display = ['car_id', 'number', 'shop','user','order','status']
    list_per_page = 10
    # 搜索字段
    search_fields = ['car_id','user']

xadmin.site.register(ShopCar, ShopCarAdmin)

class SubMenuAdmin:
    list_display = ['sub_menu_id', 'name', 'cate']
    list_per_page = 10
    # 搜索字段
    search_fields = ['name','cate']

xadmin.site.register(SubMenu, SubMenuAdmin)

class SubMenu2Admin:
    list_display = ['sub_menu2_id', 'name', 'sub_menu']
    list_per_page = 10
    # 搜索字段
    search_fields = ['name','sub_menu']

xadmin.site.register(SubMenu2, SubMenu2Admin)