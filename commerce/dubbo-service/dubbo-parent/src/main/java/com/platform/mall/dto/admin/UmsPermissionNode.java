package com.platform.mall.dto.admin;

import com.platform.mall.entity.admin.UmsPermission;
import java.util.List;

/**
 * @author AllDataDC
 */
public class UmsPermissionNode extends UmsPermission {
    public List<UmsPermissionNode> getChildren() {
        return children;
    }

    public void setChildren(List<UmsPermissionNode> children) {
        this.children = children;
    }

    private List<UmsPermissionNode> children;

}
