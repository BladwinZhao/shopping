

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0,os.path.join(BASE_DIR,'apps'))


SECRET_KEY = '6wup19pd+pfk6v8u%h^txdu+jdcj*t7xad$f-y7q9ci3-uq7xa'


DEBUG = True

ALLOWED_HOSTS = []



#系统
SYS_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
#第三方的
EXT_APPS = [
    #必要
    'xadmin',
    'crispy_forms',
    #非必要 修改样式
    'reversion',
    'django_ajax',
]


#自定义app
CUSTOM_APPS =[
    'apps.account',
    'apps.main',
    'apps.detail',
    'apps.cate',
    'apps.search',
    'apps.shopping_car',
]

INSTALLED_APPS = EXT_APPS + CUSTOM_APPS +SYS_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shopping.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'shopping.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shopping1',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': 'zwh19961221',
        'charset': 'utf8',
    }
}



AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'main.User'

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

#开启django时区 如果不需要django时区 则设置为Fasle
USE_TZ = False




STATIC_URL = '/static/'

#配置静态文件的
STATIC_ROOT ='static_root'
#配置静态文件的目录
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
    os.path.join(BASE_DIR,'apps/main/static'),
    os.path.join(BASE_DIR, 'apps/account/static'),

)

#配置访问多媒体路径

MEDIA_URL = '/media/'
#配置文件上传目录
MEDIA_ROOT = os.path.join(BASE_DIR,'media')





#=========缓存的配置=========
CACHES = {
    "default": {
        # 使用redis做缓存
        'BACKEND': 'django_redis.cache.RedisCache',
        # 将缓存的数据保存在该目录下
        # 缓存的地址
        'LOCATION': 'redis://112.74.42.138:6379/0',
        # rediss: //[:password]@localhost:6379 / 0
        'TIMEOUT': 300,
        'OPTIONS': {
            # "PASSWORD": ""
            # 是否压缩缓存数据
            # "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",
            # 配置连接池
            "CONNECTION_POOL_KWARGS": {"max_connections": 100, "retry_on_timeout": True}
        }
    },
    'session': {
        # 指定缓存的类型是文件缓存
        'BACKEND': 'django_redis.cache.RedisCache',
        # 将缓存的数据保存在该目录下
        'LOCATION': 'redis://112.74.42.138:6379/3',
        'TIMEOUT': 300,
        'OPTIONS': {
            # "PASSWORD": ""
            # 是否压缩缓存数据(非必要)
            "COMPRESSOR": "django_redis.compressors.lzma.LzmaCompressor",
            # 配置连接池
            "CONNECTION_POOL_KWARGS": {"max_connections": 100, "retry_on_timeout": True}
        }
    },
}

# session使用redis座位缓存
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session"



# ===============发送邮箱配置==========
# 发送邮件的服务器地址
EMAIL_HOST = 'smtp.163.com'
# 发送邮件端口
EMAIL_PORT = 25
# 发送邮件默认的名称
EMAIL_HOST_USER = '15570662291@163.com'
# 授权码
EMAIL_HOST_PASSWORD = 'py1805'
# 是否启用tls安全协议
EMAIL_USE_TLS = True

# 是否启用SSL安全协议
# EMAIL_USE_SSL = True
# 发送超时时间
# EMAIL_TIMEOUT =

# ===============发送邮箱配置 end ==========

#添加全局的登录地址 配合@login_required使用
LOGIN_URL='/account/login/'

#日志配置
LOGGING ={

}
