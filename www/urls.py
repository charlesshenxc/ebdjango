#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = ''

import os, re, time, base64, hashlib, logging

from transwarp.web import get, post, ctx, view, interceptor, seeother, notfound

from apis import api, Page, APIError, APIValueError, APIPermissionError, APIResourceNotFoundError

from models import User, South, North
from config import configs

_COOKIE_NAME = 'awesession'
_COOKIE_KEY = configs.session.secret

def _get_page_index():
    page_index = 1
    try:
        page_index = int(ctx.request.get('page', '1'))
    except ValueError:
        pass
    return page_index

def make_signed_cookie(id, password, max_age):
    # build cookie string by: id-expires-md5
    expires = str(int(time.time() + (max_age or 86400)))
    L = [id, expires, hashlib.md5('%s-%s-%s-%s' % (id, password, expires, _COOKIE_KEY)).hexdigest()]
    return '-'.join(L)

def parse_signed_cookie(cookie_str):
    try:
        L = cookie_str.split('-')
        if len(L) != 3:
            return None
        id, expires, md5 = L
        if int(expires) < time.time():
            return None
        user = User.get(id)
        if user is None:
            return None
        if md5 != hashlib.md5('%s-%s-%s-%s' % (id, user.password, expires, _COOKIE_KEY)).hexdigest():
            return None
        return user
    except:
        return None

def check_admin():
    user = ctx.request.user
    if user and user.admin:
        return
    raise APIPermissionError('No permission.')

@interceptor('/')
def user_interceptor(next):
    logging.info('try to bind user from session cookie...')
    user = None
    cookie = ctx.request.cookies.get(_COOKIE_NAME)
    if cookie:
        logging.info('parse session cookie...')
        user = parse_signed_cookie(cookie)
        if user:
            logging.info('bind user <%s> to session...' % user.name)
    ctx.request.user = user
    return next()

@interceptor('/plan')
def manage_interceptor(next):
    user = ctx.request.user
    if user and user.admin:
        return next()
    raise seeother('/')

def _get_southweeks_by_page():
    total = South.count_week_all('week')
    page = Page(total, _get_page_index())
    southweeks = South.find_one_column('week', 'order by week desc limit ?,?', page.offset, page.limit)
    return southweeks, page

def _get_northweeks_by_page():
    total = North.count_week_all('week')
    page = Page(total, _get_page_index())
    northweeks = North.find_one_column('week', 'order by week desc limit ?,?', page.offset, page.limit)
    return northweeks, page

@view('signin.html')
@get('/')
def signin():
    return dict()

@get('/signout')
def signout():
    ctx.response.delete_cookie(_COOKIE_NAME)
    raise seeother('/')

@view('index.html')
@get('/plan')
def index():
    return dict(user=ctx.request.user)

@view('south_add_successfully.html')
@get('/plan/south/add/successfully')
def southaddsuccessfully():
    return dict(user=ctx.request.user)

@view('north_add_successfully.html')
@get('/plan/north/add/successfully')
def northaddsuccessfully():
    return dict(user=ctx.request.user)

@view('south_change_successfully.html')
@get('/plan/south/change/successfully')
def southchangesuccessfully():
    return dict(user=ctx.request.user)

@view('north_change_successfully.html')
@get('/plan/north/change/successfully')
def northchangesuccessfully():
    return dict(user=ctx.request.user)

@view('south_delete_successfully.html')
@get('/plan/south/delete/successfully')
def southdeletesuccessfully():
    return dict(user=ctx.request.user)

@view('north_delete_successfully.html')
@get('/plan/north/delete/successfully')
def northdeletesuccessfully():
    return dict(user=ctx.request.user)

@view('south.html')
@get('/plan/south')
def south():
    return dict(page_index=_get_page_index(), action='/api/south', redirect='/plan/south/add/successfully', user=ctx.request.user)

@view('north.html')
@get('/plan/north')
def north():
    return dict(page_index=_get_page_index(), action='/api/north', redirect='/plan/north/add/successfully', user=ctx.request.user)

@view('south_plan.html')
@get('/plan/south/:south_week_id')
def southplan(south_week_id):
    southplan = South.find_by('where week=? order by site asc limit 1000', south_week_id)
    if southplan is None:
	raise notfound()
    return dict(south_week_id=south_week_id, southplan=southplan, user=ctx.request.user)

@view('north_plan.html')
@get('/plan/north/:north_week_id')
def northplan(north_week_id):
    northplan = North.find_by('where week=? order by site asc limit 1000', north_week_id)
    if northplan is None:
        raise notfound()
    return dict(north_week_id=north_week_id, northplan=northplan, user=ctx.request.user)

@view('south_edit.html')
@get('/plan/south/edit/:south_plan_id')
def southplanedit(south_plan_id):
    southplanedit = South.get(south_plan_id)
    if southplanedit is None:
        raise notfound()
    return dict(id=southplanedit.id, action='/api/south/edit/%s' % south_plan_id, redirect='/plan/south/change/successfully', user=ctx.request.user)

@view('north_edit.html')
@get('/plan/north/edit/:north_plan_id')
def northplanedit(north_plan_id):
    northplanedit = North.get(north_plan_id)
    if northplanedit is None:
        raise notfound()
    return dict(id=northplanedit.id, action='/api/north/edit/%s' % north_plan_id, redirect='/plan/north/change/successfully', user=ctx.request.user)

@view('south_delete.html')
@get('/plan/south/delete/:south_plan_id')
def southplandelete(south_plan_id):
    southplandelete = South.get(south_plan_id)
    if southplandelete is None:
        raise notfound()
    return dict(id=southplandelete.id, item=southplandelete.item, action='/api/south/delete/%s' % south_plan_id, redirect='/plan/south/delete/successfully', user=ctx.request.user)

@view('north_delete.html')
@get('/plan/north/delete/:north_plan_id')
def northplandelete(north_plan_id):
    northplandelete = North.get(north_plan_id)
    if northplandelete is None:
        raise notfound()
    return dict(id=northplandelete.id, item=northplandelete.item, action='/api/north/delete/%s' % north_plan_id, redirect='/plan/north/delete/successfully', user=ctx.request.user)

@api
@get('/api/south/edit/:south_plan_id')
def api_get_southplan(south_plan_id):
    south = South.get(south_plan_id)
    if south:
        return south
    raise APIResourceNotFoundError('South')

@api
@get('/api/north/edit/:north_plan_id')
def api_get_northplan(north_plan_id):
    north = North.get(north_plan_id)
    if north:
        return north
    raise APIResourceNotFoundError('North')

@api
@get('/api/south/weeks')
def api_get_southweeks():
    southweeks, page = _get_southweeks_by_page()
    return dict(southweeks=southweeks, page=page)

@api
@get('/api/north/weeks')
def api_get_northweeks():
    northweeks, page = _get_northweeks_by_page()
    return dict(northweeks=northweeks, page=page)

@api
@post('/api/authenticate')
def authenticate():
    i = ctx.request.input(remember='')
    username = i.username.strip().lower()
    password = i.password
    remember = i.remember
    user = User.find_first('where name=?', username)
    if user is None:
        raise APIError('auth:failed', 'username', 'Invalid username.')
    elif user.password != password:
        raise APIError('auth:failed', 'password', 'Invalid password.')
    # make session cookie:
    max_age = 604800 if remember=='true' else None
    cookie = make_signed_cookie(user.id, user.password, max_age)
    ctx.response.set_cookie(_COOKIE_NAME, cookie, max_age=max_age)
    user.password = '******'
    return user

@api
@post('/api/south')
def api_create_southplan():
    check_admin()
    i = ctx.request.input(site='', typee='', item='', progress='', details='', ttcm='', owner='')
    site = i.site.strip()
    typee = i.typee.strip()
    item = i.item.strip()
    progress = i.progress.strip()
    details = i.details.strip()
    ttcm = i.ttcm.strip()
    owner = i.owner.strip()
    if not site:
        raise APIValueError('site', 'Site is required.')
    if not typee:
        raise APIValueError('typee', 'Type is required.')
    if not item:
        raise APIValueError('item', 'Item is required.')
    if not progress:
        raise APIValueError('progress', 'Progress is required.')
    if not details:
        raise APIValueError('details', 'Details is required.')
    if not owner:
        raise APIValueError('owner', 'Owner is required.')
    user = ctx.request.user
    south = South(site=site, type=typee, item=item, progress=progress, details=details, ttcm=ttcm, owner=owner)
    south.insert()
    return south

@api
@post('/api/north')
def api_create_northplan():
    check_admin()
    i = ctx.request.input(site='', typee='', item='', progress='', details='', ttcm='', owner='')
    site = i.site.strip()
    typee = i.typee.strip()
    item = i.item.strip()
    progress = i.progress.strip()
    details = i.details.strip()
    ttcm = i.ttcm.strip()
    owner = i.owner.strip()
    if not site:
        raise APIValueError('site', 'Site is required.')
    if not typee:
        raise APIValueError('typee', 'Type is required.')
    if not item:
        raise APIValueError('item', 'Item is required.')
    if not progress:
        raise APIValueError('progress', 'Progress is required.')
    if not details:
        raise APIValueError('details', 'Details is required.')
    if not owner:
        raise APIValueError('owner', 'Owner is required.')
    user = ctx.request.user
    north = North(site=site, type=typee, item=item, progress=progress, details=details, ttcm=ttcm, owner=owner)
    north.insert()
    return north

@api
@post('/api/south/edit/:south_plan_id')
def api_update_southplan(south_plan_id):
    check_admin()
    i = ctx.request.input(site='', type='', item='', progress='', details='', ttcm='', owner='')
    site = i.site.strip()
    type = i.type.strip()
    item = i.item.strip()
    progress = i.progress.strip()
    details = i.details.strip()
    ttcm = i.ttcm.strip()
    owner = i.owner.strip()
    if not site:
        raise APIValueError('site', 'Site is required.')
    if not type:
        raise APIValueError('type', 'Type is required.')
    if not item:
        raise APIValueError('item', 'Item is required.')
    if not progress:
        raise APIValueError('progress', 'Progress is required.')
    if not details:
        raise APIValueError('details', 'Details is required.')
    if not owner:
        raise APIValueError('owner', 'Owner is required.')
    south = South.get(south_plan_id)
    if southplanedit is None:
        raise APIResourceNotFoundError('South')
    south.site = site
    south.type = type
    south.item = item
    south.progress = progress
    south.details = details
    south.ttcm = ttcm
    south.owner = owner
    south.update()
    return south

@api
@post('/api/north/edit/:north_plan_id')
def api_update_northplan(north_plan_id):
    check_admin()
    i = ctx.request.input(site='', type='', item='', progress='', details='', ttcm='', owner='')
    site = i.site.strip()
    type = i.type.strip()
    item = i.item.strip()
    progress = i.progress.strip()
    details = i.details.strip()
    ttcm = i.ttcm.strip()
    owner = i.owner.strip()
    if not site:
        raise APIValueError('site', 'Site is required.')
    if not type:
        raise APIValueError('type', 'Type is required.')
    if not item:
        raise APIValueError('item', 'Item is required.')
    if not progress:
        raise APIValueError('progress', 'Progress is required.')
    if not details:
        raise APIValueError('details', 'Details is required.')
    if not owner:
        raise APIValueError('owner', 'Owner is required.')
    north = North.get(north_plan_id)
    if northplanedit is None:
        raise APIResourceNotFoundError('North')
    north.site = site
    north.type = type
    north.item = item
    north.progress = progress
    north.details = details
    north.ttcm = ttcm
    north.owner = owner
    north.update()
    return north

@api
@post('/api/south/delete/:south_plan_id')
def api_delete_southplan(south_plan_id):
    check_admin()
    south = South.get(south_plan_id)
    if south is None:
        raise APIResourceNotFoundError('South')
    south.delete()
    return dict(id=south_plan_id)

@api
@post('/api/north/delete/:north_plan_id')
def api_delete_northplan(north_plan_id):
    check_admin()
    north = North.get(north_plan_id)
    if north is None:
        raise APIResourceNotFoundError('North')
    north.delete()
    return dict(id=north_plan_id)
